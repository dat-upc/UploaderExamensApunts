var anterior = "#" + $("#id_document option:selected").val();
$(anterior).show();
var actual = "";

$("#id_document").change(function() {
    $("#parcial_final").val("---");
    $("#tipus_examen").val("---");
    actual = "#" + $("#id_document option:selected").val();

    $(anterior).hide();
    $(actual).show();
    anterior = actual;
    actual = "";
});
 
