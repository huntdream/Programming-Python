/**
 * Created by Yu on 4/21/2017.
 */
$(document).ready(function () {
    var h1 = $('h1');
    $(h1).hide();
    $(h1).animate(
        {
            opacity: 'toggle',
            fontSize: 'toggle'
        }, 'slow');
});