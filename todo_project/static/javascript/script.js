const input_text = document.getElementById("input-box")
const list_container = document.getElementById("list-container")
let li_elements = document.getElementsByTagName("li")
function defaultTask() {
  if (input_text.value === "") {
    //alert("You must write some data")
  } else {
    // let li = document.createElement("li")
    // li.innerHTML = input_text.value
    // list_container.appendChild(li)
    // li.classList.add("unchecked");
    // let span = document.createElement("span")
    span.innerHTML = "\u00d7"
    li_elements.appendChild(span)
  }
  input_text.value = ""
  // saveData()
}

list_container.addEventListener(
  "click",
  function (e) {
    if (e.target.tagName === "LI") {
      e.target.classList.toggle("checked")
      // saveData()
    } else if (e.target.tagName === "SPAN") {
      e.target.parentElement.remove()
      // saveData()
    }
  },
  false
)

// function saveData() {
//   localStorage.setItem("data", list_container.innerHTML)
// }

// function showTask() {
//   list_container.innerHTML = localStorage.getItem("data")
// }
// showTask()
defaultTask()
