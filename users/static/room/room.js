function apiPost(url, data, onSuccess, onError) {
    $.ajax({
        url: url,
        type: "POST",
        data: JSON.stringify(data),
        contentType: "application/json",
        headers: {
            "X-CSRFToken": getCSRFToken()
        },
        success: onSuccess,
        error: function(xhr) {
            let msg = "Something went wrong!";

            try {
                let resp = JSON.parse(xhr.responseText);

                // Case 1: {"error":{"device_id":["msg"]}}
                if (resp.error) {
                    let field = Object.keys(resp.error)[0];
                    msg = resp.error[field][0];
                }
                // Case 2: {"device_id":["msg"]}  <-- DRF default
                else {
                    let field = Object.keys(resp)[0];
                    msg = resp[field][0];
                }

            } catch (e) {
                console.log("Error parsing response:", e);
            }

            Swal.fire({
                icon: "error",
                title: "Error",
                text: msg,
            });

            if (onError) onError(xhr);
        }
    });
}



    // Get CSRF Token
    function getCSRFToken() {
        return document.cookie.split(";")
            .find(c => c.trim().startsWith("csrftoken="))
            ?.split("=")[1];
    }
 
    $("#add_room_btn").click(function () {
        const roomName = $("#room_name").val().trim();
        if (!roomName) {
            Swal.fire({
                icon: "warning",
                title: "Room name required",
                text: "Please enter a room name.",
            });
            return;
        }

        apiPost("/rooms/create/", { name: roomName }, 
            function (res) {

                $("#room_name").val("");
                $("#roomModal").modal("hide");
                loadRooms();  // reload room list

                Swal.fire({
                    icon: "success",
                    title: "Room Created 🎉",
                    text: `${res.name} has been added successfully!`,
                    timer: 1500,
                    showConfirmButton: false
                });
        });
    });


      $("#openRoomModal").click(function() {
          $("#roomModal").modal("show");
      });
    
      // Base GET function
      function apiGet(url, onSuccess, onError) {
          $.ajax({
              url: url,
              type: "GET",
              contentType: "application/json",
              success: onSuccess,
              error: onError || function() { alert("Error"); }
          });
      }

      // ✅ Load rooms on page load
      function loadRooms() {
        apiGet("/rooms/list/", function(data){
            const container = $("#room_container");
            container.empty(); // Clear existing cards
            data.forEach(function(room){
                container.append(getRoomCardHTML(room));
            });
        });
    }


function findByIdRoom(room_id) {
    $.ajax({
        url: `/rooms/${room_id}/`,
        type: "GET",
        success: function(response) {

            $("#room-title").text(response.name);

            let html = "";
            response.devices.forEach(device => {
                html += `
                    <div class="col-md-12 col-xl-4">
                        <div class="card">
                            <div class="list-group list-group-flush">
                                <a href="#" class="list-group-item list-group-item-action">
                                    <div class="d-flex">
                                    <div class="flex-shrink-0">
                                        <div class="avtar avtar-s rounded-circle bg-light-dark">
                                            <i class="ti ti-bulb f-18"></i>
                                            </div>
                                        </div>
                                        <div class="flex-grow-1 ms-3">
                                            <h6 class="mb-1">${device.name} ${device.device_type}</h6>
                                            <p class="mb-0 text-muted"> ${device.state ? "ON" : "OFF"}</P>
                                        </div>
                                        <div class="flex-shrink-0 text-end">
                                        <div class="custom-switch-container">
                                                <div id="customSwitch1" class="custom-switch {% if bulb.status %}on{% endif %}">
                                                <span class="custom-switch-text-off">OFF</span>
                                                <span class="custom-switch-text-on">ON</span>
                                                </div>
                                            </div>
                                        </div>
                                
                                    </div>
                                </a>
                            </div>
                        </div>
                    </div>
                `;
            });

            $("#device-list").html(html || "<p>No devices in this room.</p>");
        },
        error: function() {
            alert("Room not found!");
        }
    });
}



function deleteRoom(roomId) {
      Swal.fire({
      title: "Are you sure?",
      text: "This action will permanently delete the room and its devices.",
      icon: "warning",
      showCancelButton: true,
      confirmButtonColor: "#d33",
      cancelButtonColor: "#3085d6",
      confirmButtonText: "Yes, delete it!"
    }).then((result) => {
      if (result.isConfirmed) {

        $.ajax({
          url: `/rooms/${roomId}/delete/`,
          type: "DELETE",
          headers: { "X-CSRFToken": getCookie("csrftoken") },
          success: function(response) {
            Swal.fire(
              "Deleted!",
              "Room has been deleted.",
              "success"
            );
            loadRooms(); // Refresh room list after delete
          },
          error: function() {
            Swal.fire(
              "Error!",
              "Something went wrong while deleting.",
              "error"
            );
          }
        });

      }
    });
  }


    // CSRF helper (if not already defined)
    function getCookie(name) {
      let cookieValue = null;
      if (document.cookie && document.cookie !== "") {
        const cookies = document.cookie.split(";");
        for (let cookie of cookies) {
          cookie = cookie.trim();
          if (cookie.startsWith(name + "=")) {
            cookieValue = cookie.substring(name.length + 1);
            break;
          }
        }
      }
      return cookieValue;
    }