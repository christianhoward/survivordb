$(document).ready(function() {
    $('.togglespoilers').click(function() {
        $('.panel').slideToggle('slow');
    });
    
    var $divs = $('div.col-xs-3');
    $('.alpha').on('click', function () {
        var alphabeticallyOrderedDivs = $divs.get().sort(function (a, b) {
            return $(a).attr('data-name').localeCompare($(b).attr('data-name'));
        });
        $('.people').empty().append(alphabeticallyOrderedDivs);
    });
    
    $('.finish').on('click', function () { 
        var numericallyOrderedDivs = $divs.get().sort(function (a, b) { 
            return $(a).attr('data-id') < $(b).attr('data-id'); 
        });
        $('.people').empty().append(numericallyOrderedDivs);
    });
    
});