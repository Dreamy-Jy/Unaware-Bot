var a = {
apiKey: "AIzaSyBWXLIWLm8rRmVJGzOpR_P6Lm58Z3Qm51I",
authDomain: "human-race.firebaseapp.com",
databaseURL: "https://human-race.firebaseio.com",
storageBucket: "human-race.appspot.com",
};
firebase.initializeApp(a);

$('#email').val('');

$(document).keypress(function(e) {
    if(e.which == 13) {
        submit();
    }
})

function submit() {
    var person = $('#email').val();
    if (person.length > 0) {
        firebase.database().ref('email/' + person).update({phone: person});
        $('#email').val('');
    }
}
