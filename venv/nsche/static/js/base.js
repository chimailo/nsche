$( document ).ready(function(){
	$(".dropdown-button").dropdown();
	$(".button-collapse").sideNav();
	$(".parallax").parallax();
	$('select').material_select();
	$('.datepicker').pickadate({
		    selectMonths: true, // Creates a dropdown to control month
		    selectYears: 1 // Creates a dropdown of 15 years to control year
	  });
	$('#id_bio', '.body').val('');
    $('#id_bio', '.body').trigger('autoresize');
    $('.collapsible').collapsible();
    $('.carousel').carousel();
});

