function roundToTwo(num) {
    return +(Math.round(num + "e+2") + "e-2");
}

/**
 * Funcion para sumar columnas de tablas basados en los td de clase sum
 * table_id El identificador de la tabla (id o clase)
 * return Un arreglo de igual tamaño que la cantidad de columnas con los valores sumados en la posicion correspondiente
 */
function sumtr(table_id) {
    var s = [];
    var r = 0;
    $(table_id + " tbody tr").each(function (index) {
        console.log($(this));
        var col = 0;
        $(this).children("td").each(function () {
            if ($(this).is(".sum")) {
                console.log($(this));
                if (s.length < col + 1) s[col] = 0;
                
                var val = parseFloat($(this).html().replace(/,/g, '').replace('$', '').replace('%', ''));

                s[col] = s[col] + val;
            } else {
                s[col] = "noCount"; // a flag which tells us we're not counting that column
            }
            col++;
        });
        r++;
    });
    $("#id_n_participantes").val(r);
    return s;
}

$('.select2').trigger('change.select2')

$('#env-sol').click(function (e) {
    e.preventDefault();
    $("#id_estado").val("SLCE");
    $("#form-fact").trigger("submit");
});

if ($('#participantes-table tbody tr').length > 0) {
    $('#env-sol').attr('disabled',false);
    
    s = sumtr("#participantes-table");
    console.log(s)
    $("#id_subtotal").val(s[3]);
    $("#id_valor_total").val(s[5]);
    $("#id_descuento_total").val((s[3] - s[5]).toFixed(2));
    $("#id_descuento_fact").val(roundToTwo(((s[3] - s[5]) / s[3]) * 100));

    // $("#subtotal").val("$ "+s[3].toFixed(2));
    // $("#valor_total").val('$ '+s[5].toFixed(2));
    // $("#descuento_total").val('$ '+(s[3] - s[5]).toFixed(2));
    $("#descuento_fact").val(roundToTwo(((s[3] - s[5]) / s[3]) * 100)+' %');

    $("#subtotal").val(s[3].toFixed(2));
    $("#valor_total").val(s[5].toFixed(2));
    $("#descuento_total").val(+(s[3] - s[5]).toFixed(2));
    back("#subtotal");
    transform("#subtotal");
    back("#valor_total");
    transform("#valor_total");
    back("#descuento_total");
    transform("#descuento_total");

}
else {
    $('#env-sol').attr('disabled',true);
    $("#id_subtotal").val(0);
    $("#id_valor_total").val(0);
    $("#id_descuento_total").val(0);
    $("#id_descuento_fact").val(0);
}

function back(input){
    const val=$(input).val();
    $(input).attr("type","number");
    $(input).val(parseFloat(val.replace(/,/g,"")));
    $(input).val(parseFloat($(input).val()).toFixed(2));
}

//Funcion para establecer Formato de Dinero
function transform(input){
    if($(input).val()!=""){
      $(input).val(parseFloat($(input).val()).toFixed(2));
    $(input).attr("type","text");
    console.log($(input).val())
    var numeroe=$(input).val().split(".")
    const long= numeroe[0].length;
    console.log(long)
    var newnum="";
    cont=0;
    for(var i=(long-1);i>=0;i--){
          if(cont%3==0 && cont!=0){
            newnum=numeroe[0].charAt(i)+","+newnum;
            console.log("coma");
            console.log(i);
            console.log(numeroe[0].charAt(i));
            cont+=1;
          }else{
            console.log("no coma");
            console.log(i);
            console.log(numeroe[0].charAt(i));
            newnum=numeroe[0].charAt(i)+newnum;
            cont+=1;
          }
    }
    console.log(newnum+"."+numeroe[1]);
    $(input).val("$"+newnum+"."+numeroe[1]);
    }
    
  }