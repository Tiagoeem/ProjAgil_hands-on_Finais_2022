function b() {
    console.log(myVar);
}

function a() {
	let myVar = 2;
	b();
}

let myVar = 1;
a();