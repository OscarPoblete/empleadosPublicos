document.addEventListener('DOMContentLoaded', function(){
    const mostrarMenu = document.getElementById('mostrarMenu');
    const menu = document.getElementById('mantenedor');

    mostrarMenu.addEventListener('click', function(){
        if (menu.style.display === 'none' || menu.style.display === ''){
            menu.style.display = 'block';
        } else {
            menu.style.display = 'none';
        }
    });


    const btnAgregar = document.getElementById('btnAgregar');
    const modal = document.getElementById('modal');
    const btnCancelar = document.getElementById('btnCancelar')

    btnAgregar.addEventListener('click', function(){
        modal.style.display = 'block';
    });

    btnCancelar.addEventListener('click', function(){
        modal.style.display = 'none';
    })
 
});


//function mostrarFormulario(button){
//    var idProyecto = button.getAttribute('data-id')
//    console.log("Mostrar formulario para modificar proyecto");
//};

//function confirmarEliminar(button){
//    var idProyecto = button.getAttribute('data-id')
 //   var confirmacion = confirm("¿Estas seguro que deseas eliminar el proyecto" + idProyecto + "?");
//    if (confirmacion){
//        console.log("Proyecto eliminado con ID" + idProyecto);
//    } else {
//       console.log("Se cancelo la eliminación del proyecto con ID" + idProyecto);
//    }
//};
    
