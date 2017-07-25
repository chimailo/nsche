$( document ).ready(function(){
	$(".dropdown-button").dropdown();
	$(".parallax").parallax();
	$('select').material_select();
	$('.datepicker').pickadate({
		    selectMonths: true, // Creates a dropdown to control month
		    selectYears: 1 // Creates a dropdown of 15 years to control year
	  });
	$('#id_interests', '#id_likes').val('');
    $('#id_interests', '#id_likes').trigger('autoresize');
    $('.collapsible').collapsible();
});
