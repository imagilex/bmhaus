Date.prototype.asMySQL = function() {
    let res = "" + this.getFullYear() + "-";
    res += ( this.getMonth() < 9 ? "0" : "" ) + ( this.getMonth() + 1 ) + "-";
    res += ( this.getDate() < 10 ? "0" : "" ) + this.getDate();
    return res;
}
Date.prototype.asMx = function() {
    let res = "";
    res += ( this.getDate() < 10 ? "0" : "" ) + this.getDate() + "/";
    res += ( this.getMonth() < 9 ? "0" : "" ) + ( this.getMonth() + 1 ) + "/" + this.getFullYear();
    return res;
}
Date.prototype.theTime = function() {
    let res = "";
    if ( this.getHours() < 10 ) {
        res += "0";
    }
    res += this.getHours() + ":";
    if ( this.getMinutes() < 10 ) {
        res += "0";
    }
    res += this.getMinutes();
    return res;
}

class clsApp {
    checkInputIn( idcontainer ) {
        $( '#' + idcontainer + ' input[type="checkbox"]' ).attr( 'checked', true );
    }
    uncheckInputIn( idcontainer ) {
        $( '#' + idcontainer + ' input[type="checkbox"]' ).attr( 'checked', false );
    }
    openPanel( body, title, close = true, footer = null ) {
        let template = Handlebars.compile( $( "#modal-panel-message-template" ).html() );
        let html = template( { title, body, footer, close } );
        $( "#modal-panel-message" ).remove();
        $( document.body ).append( $( html ) );
        $( "#modal-panel-message" ).modal();
    }
    setUIControls() {
        if( req_ui ) {
            $.datepicker.setDefaults( $.datepicker.regional[ "es" ] );
            $( `input[type="date"]` ).datepicker( {
                changeMonth: true,
                changeYear: true,
                dateFormat : 'yy-mm-dd'  
            } );
        }
    }
    setReadOnlyForm( container_selector = "#main-form" ) {
        let frm = $( container_selector );
        frm.find( "input" ).attr( "disabled", true );
        frm.find( "textarea" ).attr( "disabled", true );
        frm.find( "button" ).attr( "disabled", true );
        frm.find( "select" ).attr( "disabled", true );
        frm.find( "input" ).attr( "readonly", true );
        frm.find( "textarea" ).attr( "readonly", true );
        frm.find( "button" ).attr( "readonly", true );
        frm.find( "select" ).attr( "readonly", true );
        frm.find( "#btn-save" ).remove();
    }
    showPrivacyPolicy(){
        App.openPanel( $( "#privacy-policy-template" ).html(), "Política de Privacidad" );
    }
}

class clsCliente {
    showFrmDireccionCasaAdd() {
        App.openPanel(
            $( "#direccion-casa-template" ).html(),
            "Agregar Dirección de Casa"
        )
        $( '#main-form input[name=action]' )[0].value="add-home-add";
    }
    showFrmDireccionCasaUpd() {
        App.openPanel(
            $( "#direccion-casa-template" ).html(),
            "Actualizar Dirección de Casa"
        )
        $( '#main-form input[name=action]' )[0].value="upd-home-add";
    }
    showFrmDireccionOficinaAdd() {
        App.openPanel(
            $( "#direccion-oficina-template" ).html(),
            "Agregar Dirección de Oficina"
        )
        $( '#main-form input[name=action]' )[0].value="add-office-add";
    }
    showFrmDireccionOficinaUpd() {
        App.openPanel(
            $( "#direccion-oficina-template" ).html(),
            "Actualizar Dirección de Oficina"
        )
        $( '#main-form input[name=action]' )[0].value="upd-office-add";
    }
    showNotasSglCte() {
        App.openPanel( $( "#notas-template" ).html(), "Notas del Cliente" );
    }
    showNotasCte(idcte,nombre) {
        App.openPanel( $( "#notas-template" ).html(), "Notas: " + nombre );
        $( "#notas-cliente" ).html( $( "#notas-cte-" + idcte + "-template" ).html() );
        $( "#nota_cte" ).attr( 'value', idcte );
    }
}

let App = new clsApp();
let Cte = new clsCliente();

$( document ).ready( () => { 
    $('[data-toggle="tooltip"]').tooltip(); 
    App.setUIControls();
} );

