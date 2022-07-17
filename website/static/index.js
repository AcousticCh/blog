document.addEventListener("click", e => {
	const isDropdownButton = e.target.matches("[data-dropdown-button]")
	if(!isDropdownButton && e.target.closest("[data-dropdown]") != null) return
	
	let currentDropdown
	if(isDropdownButton){
		currentDropdown = e.target.closest("[data-dropdown]")
		currentDropdown.classList.toggle("active")
	}
	
	document.querySelectorAll("[data-dropdown].active").forEach(dropdown =>{
		if(dropdown === currentDropdown) return
		dropdown.classList.remove("active")
		})
})

function deletePage(pageId) {
    fetch("/delete-page", {
        method: "POST",
        body: JSON.stringify({pageId: pageId}),
    }).then((_res) => {
        window.location.href = "/";
    });
}

function submitSignupForm() {
	document.getElementById("signup-form").submit();
}

function submitSigninForm() {
	document.getElementById("signin-form").submit();
}

function submitNewPage() {
	document.querySelector(".page-container").submit();
}