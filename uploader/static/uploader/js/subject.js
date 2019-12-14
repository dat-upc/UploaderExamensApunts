/* Copyright (C) 2019 Aniol Marti
* This file is part of DAT - UploaderExamensApunts.
*
* DAT - UploaderExamensApunts is free software: you can redistribute it and/or modify
* it under the terms of the GNU Affero General Public License as published by
* the Free Software Foundation, either version 3 of the License, or
* (at your option) any later version.
*
* DAT - UploaderExamensApunts is distributed in the hope that it will be useful,
* but WITHOUT ANY WARRANTY; without even the implied warranty of
* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
* GNU Affero General Public License for more details.
*
* You should have received a copy of the GNU Affero General Public License
* along with DAT - UploaderExamensApunts. If not, see <https://www.gnu.org/licenses/>.
*/
var assig_anterior;
var assig_actual;

$("#id_grau").change(function() {
    $("#assignatura").hide();
    assig_actual = "#" + "assig" + $("#id_grau option:selected").val();
    if ($("#id_grau option:selected").val() == "") $("#assignatura").show();

    $(assig_anterior).hide();
    $(assig_actual).show();
    assig_anterior = assig_actual;
    assig_actual = "";
});
