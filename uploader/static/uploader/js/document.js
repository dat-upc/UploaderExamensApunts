var anterior = "#" + $("#show option:selected").val();
$(anterior).show();
var actual = "";

$("#show").change(function() {
    $("#ParcialOFinal").val("---");
    $("#TipusExamen").val("---");
    actual = "#" + $("#show option:selected").val();

    $(anterior).hide();
    $(actual).show();
    anterior = actual;
    actual = "";
});
 
