var anterior = "#" + $("#document option:selected").val();
$(anterior).show();
var actual = "";

$("#document").change(function() {
    $("#ParcialOFinal").val("---");
    $("#TipusExamen").val("---");
    actual = "#" + $("#document option:selected").val();

    $(anterior).hide();
    $(actual).show();
    anterior = actual;
    actual = "";
});
 
