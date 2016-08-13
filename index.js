var a = {
apiKey: "AIzaSyBWXLIWLm8rRmVJGzOpR_P6Lm58Z3Qm51I",
authDomain: "human-race.firebaseapp.com",
databaseURL: "https://human-race.firebaseio.com",
storageBucket: "human-race.appspot.com",
};
firebase.initializeApp(a);

var email = firebase.database().ref('email/');

function submit() {
    var person = $('#email').val();
    email.push({
        phone: person
    })
}
