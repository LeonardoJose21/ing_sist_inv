
const author_2_id = document.getElementById("author_2_id");
const author_2_name = document.getElementById("author_2_name");
const author_2_email = document.getElementById("author_2_email");

const author_3_id = document.getElementById("author_3_id");
const author_3_name = document.getElementById("author_3_name");
const author_3_email = document.getElementById("author_3_email");

  // Add event listeners to the input elements
  author_2_id.addEventListener("input", addRequiredPropperty_2);
//   author_2_name.addEventListener("input", addRequiredPropperty_2);
//   author_2_email.addEventListener("input", addRequiredPropperty_2);
  author_3_id.addEventListener("input", addRequiredPropperty_3);
//   author_3_name.addEventListener("input", toggleRequired);
//   author_3_email.addEventListener("input", toggleRequired);
  // Function to toggle the 'required' attribute based on input values
  function addRequiredPropperty_2() {
    if (author_2_id.value.trim() !== "") {
        author_2_name.setAttribute("required", "");
        author_2_email.setAttribute("required", "");
    } 
  }

  function addRequiredPropperty_3() {
    if (author_3_id.value.trim() !== "") {
        author_3_name.setAttribute("required", "");
        author_3_email.setAttribute("required", "");
    } 
  }
