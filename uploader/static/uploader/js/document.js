var anterior;
var actual;

$("#id_document").change(function() {
    $("#id_parcial_final").val("");
    $("#id_tipus_examen").val("");
    actual = "#" + $("#id_document option:selected").val();

    $(anterior).hide();
    $(actual).show();
    anterior = actual;
    actual = "";
});