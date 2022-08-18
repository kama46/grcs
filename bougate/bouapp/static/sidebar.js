var btn = document.querySelector("#btn");
var sidebar = document.querySelector(".sidebar");
var content = document.querySelector(".content");

btn.onclick = function()
{
    sidebar.classList.toggle("active");
    content.classList.toggle("active");
    // alert("success");
}
