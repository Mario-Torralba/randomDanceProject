// ***********************************************************
// FUNCION AJAX

// function comprobacionEmpleado(email) {

//     $.ajax({
//         url: 'Controller',
//         data: {
//             ACTION: "USER.COMPROBADO",
//             EMAIL: email
//         },
//         dataType: 'json',
//         success: function (responseText) {


//             controllerResponse("USER.COMPROBADO", responseText)

//         }
//     });

// }

document.body.addEventListener("load", initComponents())

function initComponents(){

    const botonForm = document.getElementById('botonInputs')

    botonForm.addEventListener('click',()=>{
        let inputGrupo = document.getElementById('inputGrupo')
        let inputCancion = document.getElementById('inputCancion')

        findAll(inputGrupo.value,inputCancion.value)
    })
}

function findAll(grupo,cancion) {
    alert('entrada ajax')
    $.ajax({
        url: 'Controller',
        data: {
            ACTION: "USUARIO.FINDALL",
            GRUPO: grupo,
            CANCION: cancion
        },
        dataType: 'json',
        success: function (responseText) {

            console.log(responseText)

        }
    });

}
