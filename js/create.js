function guardar() {
 
    let n = document.getElementById("txtNombre").value
    let p = parseFloat(document.getElementById("txtPrecio").value)
    let s = parseInt(document.getElementById("txtStock").value)
    let d = document.getElementById("txtDesc").value
    let i = document.getElementById("txtImg").value

 
    let producto = {
        nombre: n,
        precio: p,
        stock: s,
        desc: d,
        imgurl: i
    }
    let url = "https://crud-shop-flask.herokuapp.com/productos"
    var options = {
        body: JSON.stringify(producto),
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
       // redirect: 'follow'
    }
    fetch(url, options)
    .then(function () {
        console.log("creado")
        alert("Grabado")

        // Handle response we get from the API
    })
    .catch(err => {
        //this.errored = true
        alert("Error al grabar" )
        console.error(err);
    })
}

