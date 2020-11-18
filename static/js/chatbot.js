var former_messages = document.getElementById("former_messages");
var new_answers = document.getElementById("new_answers_ul");
var send_button = document.getElementById("send_button");
var id_answer = 0;

// Initialisation:
let block_conv1 = [];

function bot_asks(question, answers){
    let new_question = document.createElement('div');
    new_question.classList.add('bot_question');
    let question_blocks = question.split(' - ')[2].split(' \n ');
    for (let question_block of question_blocks) {
        new_p = document.createElement('p');
        new_p.textContent = question_block;
        new_question.appendChild(new_p);
    }
    new_question.style.backgroundColor = '#ddd';
    former_messages.appendChild(new_question);
    for (let answer of answers){
        let new_li = document.createElement('li');
        new_li.classList.add('answer_li');
        let new_answer = document.createElement('input');
        new_answer.setAttribute('type', 'checkbox');
        new_answer.setAttribute('name', 'answer');
        let answer_id = question.split(' - ')[0] + '-' + question.split(' - ')[0] + '-' + answer[0];
        new_answer.setAttribute('value', answer_id);
        new_answer.id = answer_id
        new_answer_label = document.createElement('label');
        new_answer_label.setAttribute('for', answer_id);
        new_answer_label.textContent = answer.slice(4);
        new_answer_label.id = answer_id + '_label'
        new_li.appendChild(new_answer);
        new_li.appendChild(new_answer_label);
        new_answers.appendChild(new_li);
    }
}

function send_answer(answer_id){
    let new_answer = document.createElement('div');
    new_answer.classList.add('user_answer');
    let good_answer = document.getElementById(answer_id + '_label');
    new_answer.textContent = good_answer.textContent;
    new_answer.style.backgroundColor = '#afeeee';
    former_messages.appendChild(new_answer);
}

send_button.addEventListener('click', function(){
    let answers = document.getElementsByName('answer');
    let selected_answers = false;
    for (let answer of answers){
        if (answer.checked === true){
            send_answer(answer.value);
            selected_answers = true;
            block_conv1 = block_conv1.concat([answer.value]);
        }
    }
    if (selected_answers) {
        while (new_answers.childNodes.length > 0){
            new_answers.removeChild(new_answers.childNodes[0])
        }
    }
})



console.log("ce script n'est pas bugué")
//bot_asks('0 - 0 - comment ça va? \n Je me posais la question!', ['1 - Bien', '2 - Pas Bien'])

/* === Block One === */


block_question1 = new Map()
block_answer1 = new Map()


block_question1.set(0, "1 - 0 - J’aimerais mieux comprendre si vous vous sentez épuisé.e émotionnellement. Quelle(s) proposition(s) s’applique à votre état actuel ? \n (Plusieurs choix possibles)");

block_answer1.set(0, ["1 - Je me sens émotionnellement vidé(e) par mon travail", "2 - Je me sens à bout à la fin de ma journée de travail",
"3 - Je me sens fatigué lorsque je me lève le matin et que j’ai à affronter une autre journée de travail ",
"4 - Travailler avec des gens tout au long de la journée me demande des efforts", "5 - Je me sens au bout du rouleau"])

block_question1.set(1, "1 - 1 - Dites-moi en plus sur votre niveau d’épuisement émotionnel. Quelle(s) phrases correspondent actuellement ? \n (Plusieurs choix possibles)");

block_answer1.set(1, ["1 - Je me sens frustré(e) par mon travail", "2 - Je sens que je travaille “trop dur” dans mon travail", "3 - Travailler en contact direct avec les gens me stresse trop",
"4 - Je sens que je craque à cause de mon travail"]);

block_question1.set(2, "1 - 2 - Il reste à savoir si vous expérimentez ce que l’on pourrait appeler une “dépersonnalisation”. Parmi les propositions suivantes, quelles sont celles qui vous correspondent ? \n (Plusieurs choix possibles)")

block_answer1.set(2, ["1 - Je sens que je m’occupe de certains patients/clients/élèves de façon impersonnelle comme s’ils étaient des objets",
"2 - Je suis devenu plus insensible aux gens depuis que j’ai ce travail", "3 - Je crains que ce travail ne m’endurcisse émotionnellement ",
"4 - Je ne me soucie pas vraiment de ce qui arrive à mes patients/clients/élèves", "5 - J’ai l’impression que mes patients/clients/élèves me rendent responsable de certains de leurs problèmes"]);

block_question1.set(3, "1 - 3 - J’aimerais maintenant en savoir plus long sur votre accomplissement personnel perçu. Parmi les propositions suivantes, quelles sont celles qui s’accordent le plus avec votre expérience personnelle ? \n (Plusieurs choix possibles) ");

block_answer1.set(3, ["1 - J'ai du mal à m’occuper très efficacement des problèmes de mes clients/collègues ",
"2 - J’ai l’impression de ne pas avoir d'influence positive sur les gens à travers mon travail", "3 - Je me sens rarement plein(e) d'énergie ",
"4 - J’ai accompli peu de choses qui en valent la peine dans mon travail"]);

block_question1.set(4, "1 - 4 - Je voudrais mieux comprendre votre rapport émotionnel aux autres dans votre travail. Quelle(s) phrase(s) vous semblent vraies pour votre cas ? \n (Plusieurs choix possibles)");

block_answer1.set(4, ["1 - J'ai du mal à comprendre ce que mes clients/collègues ressentent", "2 - Je n'arrive pas à créer une atmosphère détendue avec mes clients/collègues",
"3 - Je me sens épuisé(e) lorsque dans mon travail j’ai été proche de mes clients/collègues", "4 - Dans mon travail, je peine à traiter les problèmes émotionnels avec calme"]);

block_question1.set(5, "1 - 5 - Sur une échelle allant de 0 à 10, quelle est selon vous l’intensité de ces effets négatifs ? ");

let str_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
for (let i=1; i<11; i++){
    str_num[i-1] = i.toString() + ' - ' + i.toString()
}
block_answer1.set(5, str_num);

block_question1.set(6, "1 - 6 - Il semblerait que vous ne vous épanouissez pas pleinement au travail. Depuis combien de temps ressentez-vous ces effets négatifs ?");

block_answer1.set(6, ["1 - Moins d'un jour", "2 - Entre 1 et 7 jours", "3 - Entre 1 semaine et 1 mois"]);

block_question1.set(7, "1 - 7 - Pour affiner mon diagnostic, j’aurais besoin de quelques précisions. Pour cela, je vous invite à sélectionner les informations qui s’appliquent à votre cas : \n (Plusieurs choix possibles)")

block_answer1.set(7, ["1 - Conflit de valeur et travail mal fait", "2 - Existence d’un événement récent grave (perte d’un être cher…)", "3 - Peur de l’avenir, de la mort, du changement, de l’entourage (tristesse existentielle)"])


bot_asks(block_question1.get(0), block_answer1.get(0));



