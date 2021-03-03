ClassicEditor
    .create( document.querySelector( '#id_content' ))
    .catch( error => {
        console.error( error );
    } );