
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
