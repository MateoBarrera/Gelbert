function ActivateLink(section) {
	document.getElementById("I-" + section).setAttribute("class", "setting-dashboard-item active")
};

function sendDataToBackendAjax(event, status) {
	// create own form in memory
	const formData = new FormData()

	// set values in this form
	document.getElementById("status_system").value = status
	formData.append("system", status)

	fetch("/system", {
		method: "POST",
		body: formData,
		//headers: {'Content-Type': 'application/json'},
		//body: JSON.stringify(formData)
	})
		.then(function (response) {
			data = response.json() // get result from server as JSON
			return data
		})
		.then(function (data) {
			if (data['result']) {
				Swal.fire(
					"Successfully executed!", 
					data['info'], 
					"success");
				if (status==='Start'){
					document.getElementById("status_system").value = 'Running'
				}
				else{
					document.getElementById("status_system").value = "Stopped"
				}
			}else{
				Swal.fire({
					icon: 'error',
					title: 'Oops...',
					text: 'Something went wrong!',
					footer: data['info']
				});
			};

		})
		.catch((error) => {
			Swal.fire({
				icon: "error",
				title: "Oops...",
				text: "Something went wrong!",
				footer: error,
			})
		})

	event.preventDefault() // don't send in normal way and don't reload page
};
