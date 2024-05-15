console.log('Funcionando')
document.querySelector('#boton').addEventListener('click', traerDatos);

function traerDatos(){
    const xhttp = new XMLHttpRequest();

    xhttp.open('GET', 'js/test.json', true)
    xhttp.send();
    xhttp.onreadystatechange = function(){
        if(this.readyState == 4 && this.status == 200){
            // console.log(this.responseText);
            let datos = JSON.parse(this.responseText);
            // console.log(datos);
            let res = document.querySelector('#res');
            res.innerHTML = '';

            for(let item of datos){
                // console.log(item.key);
                res.innerHTML += `
                <tr>
                    <td>${item.key}</td>
                    <td>${item.value}</td>
                    <td>${item.datetime}</td>
                </tr>
                `

            }
        }
    }

}