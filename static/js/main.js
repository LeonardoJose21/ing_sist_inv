
// function to taggle the side bar
const button = document.getElementById("StudentSidebarToggle")

if (button) {
    button.addEventListener("click", function () {

        var sidebar_student = document.getElementById("sidebar_student");
        sidebar_student.classList.toggle("-translate-x-full")
    })
}
else {
    document.getElementById("AdminSidebarToggle").addEventListener("click", function () {

        var sidebar_admin = document.getElementById("sidebar_admin");
        sidebar_admin.classList.toggle("-translate-x-full");
    })
   
}