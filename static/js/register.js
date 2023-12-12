async function register(){
    const login = document.getElementById("login").value;
    const password = document.getElementById("password").value;
    const response = await fetch("/register", {
         method: "POST",
         headers: { "Accept": "application/json", "Content-Type": "application/json" },
         body: JSON.stringify({
                username: login,
                userpass: password
         })
    });
    if (response.ok) {
        const data = await response.json();
        console.log(data);
        document.getElementById("message").textContent = "Registration Ok";
    }
    else
        console.log(response);
}