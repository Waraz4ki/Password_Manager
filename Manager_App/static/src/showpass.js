function showpass() {
    var key_input = document.getElementById("master_key");
    if (key_input.type === "password") {
      key_input.type = "text";
    } else {
      key_input.type = "password";
    }
} 