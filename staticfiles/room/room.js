
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
            error: onError || function() {
                alert("Something went wrong!");
            }
        });
    }

    // Get CSRF Token
    function getCSRFToken() {
        return document.cookie.split(";")
            .find(c => c.trim().startsWith("csrftoken="))
            ?.split("=")[1];
    }
 
      $("#add_room_btn").click(function(){
          const roomName = $("#room_name").val().trim();
          if (!roomName) return alert("Enter room name");

          apiPost("/rooms/create/", { name: roomName }, function(res){
              $("#room_name").val("");
              $("#roomModal").modal("hide");
              loadRooms();  // Reload room list after adding
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
