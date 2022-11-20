// -- Round 1 Teams --
const R1T1 = document.getElementById("R1T1");
const R1T2 = document.getElementById("R1T2");
const R1T3 = document.getElementById("R1T3");
const R1T4 = document.getElementById("R1T4");
const R1T5 = document.getElementById("R1T5");
const R1T6 = document.getElementById("R1T6");
const R1T7 = document.getElementById("R1T7");
const R1T8 = document.getElementById("R1T8");
const R1T9 = document.getElementById("R1T9");
const R1T10 = document.getElementById("R1T10");
const R1T11 = document.getElementById("R1T11");
const R1T12 = document.getElementById("R1T12");
const R1T13 = document.getElementById("R1T13");
const R1T14 = document.getElementById("R1T14");
const R1T15 = document.getElementById("R1T15");
const R1T16 = document.getElementById("R1T16");

// -- Round 2 Teams --
const R2T1 = document.getElementById("R2T1");
const R2T2 = document.getElementById("R2T2");
const R2T3 = document.getElementById("R2T3");
const R2T4 = document.getElementById("R2T4");
const R2T5 = document.getElementById("R2T5");
const R2T6 = document.getElementById("R2T6");
const R2T7 = document.getElementById("R2T7");
const R2T8 = document.getElementById("R2T8");

// -- Round 3 Teams --
const R3T1 = document.getElementById("R3T1");
const R3T2 = document.getElementById("R3T2");
const R3T3 = document.getElementById("R3T3");
const R3T4 = document.getElementById("R3T4");

// -- Round 4 Teams --
const R4T1 = document.getElementById("R4T1");
const R4T2 = document.getElementById("R4T2");

// -- Hidden Inputs --
const HI1 = document.getElementById("series1");
const HI2 = document.getElementById("series2");
const HI3 = document.getElementById("series3");
const HI4 = document.getElementById("series4");
const HI5 = document.getElementById("series5");
const HI6 = document.getElementById("series6");
const HI7 = document.getElementById("series7");
const HI8 = document.getElementById("series8");
const HI9 = document.getElementById("series9");
const HI10 = document.getElementById("series10");
const HI11 = document.getElementById("series11");
const HI12 = document.getElementById("series12");
const HI13 = document.getElementById("series13");
const HI14 = document.getElementById("series14");
const HI15 = document.getElementById("series15");

var AllHiddenInputs = [HI1,HI2,HI3,HI4,HI5,HI6,HI7,HI8,HI9,HI10,HI11,HI12,HI13,HI14,HI15];
var R2HiddenInputs = [HI9,HI9,HI10,HI10,HI11,HI11,HI12,HI12];
var R3HiddenInputs = [HI13,HI13,HI14,HI14];
var R4HiddenInputs = [HI15,HI15];

var ResetTeams = [R2T1,R2T2,R2T3,R2T4,R2T5,R2T6,R2T7,R2T8,R3T1,R3T2,R3T3,R3T4,R4T1,R4T2];
var AllTeams = [R1T1,R1T2,R1T3,R1T4,R1T5,R1T6,R1T7,R1T8,R1T9,R1T10,R1T11,R1T12,R1T13,R1T14,R1T15,R1T16,R2T1,R2T2,R2T3,R2T4,R2T5,R2T6,R2T7,R2T8,R3T1,R3T2,R3T3,R3T4,R4T1,R4T2];

var Round1Teams = [R1T1,R1T2,R1T3,R1T4,R1T5,R1T6,R1T7,R1T8,R1T9,R1T10,R1T11,R1T12,R1T13,R1T14,R1T15,R1T16];
var Round2Teams = [R2T1,R2T2,R2T3,R2T4,R2T5,R2T6,R2T7,R2T8];
var Round3Teams = [R3T1,R3T2,R3T3,R3T4];
var Round4Teams = [R4T1,R4T2];

function Master() {
  for (let i=0; i<AllTeams.length; i++) {
    AllTeams[i].disabled = true;}
}

function Submission() {
  for (let i=0; i<AllTeams.length; i++) {
    AllTeams[i].disabled = false;}
}

function Winner(id) {
  if (id.innerHTML != "") {
    id.classList.remove("loser");
    id.classList.add("winner");}
}

function Loser(id) {
    id.classList.remove("winner");
    id.classList.add("loser");
}

function ClearRound2Wins(id) {
  for (let i=0; i<Round2Teams.length; i++) {
    if (Round2Teams[i].innerHTML == id.innerHTML) {
      if (Round2Teams[i].classList.contains("winner")) {
        R2HiddenInputs[i].value = "";
      }
      Round2Teams[i].innerHTML = "";
      Round2Teams[i].classList.remove("loser","winner");}
  }
}

function ClearRound3Wins(id) {
  for (let i=0; i<Round3Teams.length; i++) {
    if (Round3Teams[i].innerHTML == id.innerHTML) {
      if (Round3Teams[i].classList.contains("winner")) {
        R3HiddenInputs[i].value = "";
      }
      Round3Teams[i].innerHTML = "";
      Round3Teams[i].classList.remove("loser","winner");}
  }
}

function ClearRound4Wins(id) {
  for (let i=0; i<Round4Teams.length; i++) {
    if (Round4Teams[i].innerHTML == id.innerHTML) {
      if (Round4Teams[i].classList.contains("winner")) {
        R4HiddenInputs[i].value = "";
      }
      Round4Teams[i].innerHTML = "";
      Round4Teams[i].classList.remove("loser","winner");}
  }
}

function ClearField(name) {
  if (name.value == "Type first and last name...") {
    name.value = "";}
}

function ResetBracket() {
  for (let i=0; i<ResetTeams.length; i++) {
    ResetTeams[i].innerHTML = "";}

  for (let i=0; i<AllHiddenInputs.length; i++) {
    AllHiddenInputs[i].value = "";}

  for (let i=0; i<AllTeams.length; i++) {
    AllTeams[i].classList.remove("winner");
    AllTeams[i].classList.remove("loser");}
}

const messagebox = document.getElementById("closediv");

function CloseMessageBox() {
  messagebox.style.display="none";}

// series 1
R1T1.addEventListener("click", function G1T1() {
  Winner(R1T1); Loser(R1T2); ClearRound2Wins(R1T2); ClearRound3Wins(R1T2); ClearRound4Wins(R1T2);
  R2T1.innerHTML = R1T1.innerHTML; document.getElementById("series1").value = R1T1.innerHTML;});
R1T2.addEventListener("click", function G1T2() {
  Winner(R1T2); Loser(R1T1); ClearRound2Wins(R1T1); ClearRound3Wins(R1T1); ClearRound4Wins(R1T1);
  R2T1.innerHTML = R1T2.innerHTML; document.getElementById("series1").value = R1T2.innerHTML;});

// series 2
R1T3.addEventListener("click", function G2T1() {
  Winner(R1T3); Loser(R1T4); ClearRound2Wins(R1T4); ClearRound3Wins(R1T4); ClearRound4Wins(R1T4);
  R2T2.innerHTML = R1T3.innerHTML; document.getElementById("series2").value = R1T3.innerHTML;});
R1T4.addEventListener("click", function G2T2() {
  Winner(R1T4); Loser(R1T3); ClearRound2Wins(R1T3); ClearRound3Wins(R1T3); ClearRound4Wins(R1T3);
  R2T2.innerHTML = R1T4.innerHTML; document.getElementById("series2").value = R1T4.innerHTML;});

// series 3
R1T5.addEventListener("click", function G3T1() {
  Winner(R1T5); Loser(R1T6); ClearRound2Wins(R1T6); ClearRound3Wins(R1T6); ClearRound4Wins(R1T6);
  R2T3.innerHTML = R1T5.innerHTML; document.getElementById("series3").value = R1T5.innerHTML;});
R1T6.addEventListener("click", function G3T2() {
  Winner(R1T6); Loser(R1T5); ClearRound2Wins(R1T5); ClearRound3Wins(R1T5); ClearRound4Wins(R1T5);
  R2T3.innerHTML = R1T6.innerHTML; document.getElementById("series3").value = R1T6.innerHTML;});

// series 4
R1T7.addEventListener("click", function G4T1() {
  Winner(R1T7); Loser(R1T8); ClearRound2Wins(R1T8); ClearRound3Wins(R1T8); ClearRound4Wins(R1T8);
  R2T4.innerHTML = R1T7.innerHTML; document.getElementById("series4").value = R1T7.innerHTML;});
R1T8.addEventListener("click", function G4T2() {
  Winner(R1T8); Loser(R1T7); ClearRound2Wins(R1T7); ClearRound3Wins(R1T7); ClearRound4Wins(R1T7);
  R2T4.innerHTML = R1T8.innerHTML; document.getElementById("series4").value = R1T8.innerHTML;});

// series 5
R1T9.addEventListener("click", function G5T1() {
  Winner(R1T9); Loser(R1T10); ClearRound2Wins(R1T10); ClearRound3Wins(R1T10); ClearRound4Wins(R1T10);
  R2T5.innerHTML = R1T9.innerHTML; document.getElementById("series5").value = R1T9.innerHTML;});
R1T10.addEventListener("click", function G5T2() {
  Winner(R1T10); Loser(R1T9); ClearRound2Wins(R1T9); ClearRound3Wins(R1T9); ClearRound4Wins(R1T9);
  R2T5.innerHTML = R1T10.innerHTML; document.getElementById("series5").value = R1T10.innerHTML;});

// series 6
R1T11.addEventListener("click", function G6T1() {
  Winner(R1T11); Loser(R1T12); ClearRound2Wins(R1T12); ClearRound3Wins(R1T12); ClearRound4Wins(R1T12);
  R2T6.innerHTML = R1T11.innerHTML; document.getElementById("series6").value = R1T11.innerHTML;});
R1T12.addEventListener("click", function G6T2() {
  Winner(R1T12); Loser(R1T11); ClearRound2Wins(R1T11); ClearRound3Wins(R1T11); ClearRound4Wins(R1T11);
  R2T6.innerHTML = R1T12.innerHTML; document.getElementById("series6").value = R1T12.innerHTML;});

// series 7
R1T13.addEventListener("click", function G7T1() {
  Winner(R1T13); Loser(R1T14); ClearRound2Wins(R1T14); ClearRound3Wins(R1T14); ClearRound4Wins(R1T14);
  R2T7.innerHTML = R1T13.innerHTML; document.getElementById("series7").value = R1T13.innerHTML;});
R1T14.addEventListener("click", function G7T2() {
  Winner(R1T14); Loser(R1T13); ClearRound2Wins(R1T13); ClearRound3Wins(R1T13); ClearRound4Wins(R1T13);
  R2T7.innerHTML = R1T14.innerHTML; document.getElementById("series7").value = R1T14.innerHTML;});

// series 8
R1T15.addEventListener("click", function G8T1() {
  Winner(R1T15); Loser(R1T16); ClearRound2Wins(R1T16); ClearRound3Wins(R1T16); ClearRound4Wins(R1T16);
  R2T8.innerHTML = R1T15.innerHTML; document.getElementById("series8").value = R1T15.innerHTML;});
R1T16.addEventListener("click", function G8T2() {
  Winner(R1T16); Loser(R1T15); ClearRound2Wins(R1T15); ClearRound3Wins(R1T15); ClearRound4Wins(R1T15);
  R2T8.innerHTML = R1T16.innerHTML; document.getElementById("series8").value = R1T16.innerHTML;});

// -- End Round 1 --


// series 9
R2T1.addEventListener("click", function G9T1() {
  Winner(R2T1); Loser(R2T2); ClearRound3Wins(R2T2); ClearRound4Wins(R2T2);
  R3T1.innerHTML = R2T1.innerHTML; document.getElementById("series9").value = R2T1.innerHTML;});
R2T2.addEventListener("click", function G9T2() {
  Winner(R2T2); Loser(R2T1); ClearRound3Wins(R2T1); ClearRound4Wins(R2T1);
  R3T1.innerHTML = R2T2.innerHTML; document.getElementById("series9").value = R2T2.innerHTML;});

// series 10
R2T3.addEventListener("click", function G10T1() {
  Winner(R2T3); Loser(R2T4); ClearRound3Wins(R2T4); ClearRound4Wins(R2T4);
  R3T2.innerHTML = R2T3.innerHTML; document.getElementById("series10").value = R2T3.innerHTML;});
R2T4.addEventListener("click", function G10T2() {
  Winner(R2T4); Loser(R2T3); ClearRound3Wins(R2T3); ClearRound4Wins(R2T3);
  R3T2.innerHTML = R2T4.innerHTML; document.getElementById("series10").value = R2T4.innerHTML;});

// series 11
R2T5.addEventListener("click", function G11T1() {
  Winner(R2T5); Loser(R2T6); ClearRound3Wins(R2T6); ClearRound4Wins(R2T6);
  R3T3.innerHTML = R2T5.innerHTML; document.getElementById("series11").value = R2T5.innerHTML;});
R2T6.addEventListener("click", function G11T2() {
  Winner(R2T6); Loser(R2T5); ClearRound3Wins(R2T5); ClearRound4Wins(R2T5);
  R3T3.innerHTML = R2T6.innerHTML; document.getElementById("series11").value = R2T6.innerHTML;});

// series 12
R2T7.addEventListener("click", function G12T1() {
  Winner(R2T7); Loser(R2T8); ClearRound3Wins(R2T8); ClearRound4Wins(R2T8);
  R3T4.innerHTML = R2T7.innerHTML; document.getElementById("series12").value = R2T7.innerHTML;});
R2T8.addEventListener("click", function G12T2() {
  Winner(R2T8); Loser(R2T7); ClearRound3Wins(R2T7); ClearRound4Wins(R2T7);
  R3T4.innerHTML = R2T8.innerHTML; document.getElementById("series12").value = R2T8.innerHTML;});

// -- End Round 2 --


// series 13
R3T1.addEventListener("click", function G13T1() {
  Winner(R3T1); Loser(R3T2); ClearRound4Wins(R3T2);
  R4T1.innerHTML = R3T1.innerHTML; document.getElementById("series13").value = R3T1.innerHTML;});
R3T2.addEventListener("click", function G13T2() {
  Winner(R3T2); Loser(R3T1); ClearRound4Wins(R3T1);
  R4T1.innerHTML = R3T2.innerHTML; document.getElementById("series13").value = R3T2.innerHTML;});

// series 14
R3T3.addEventListener("click", function G14T1() {
  Winner(R3T3); Loser(R3T4); ClearRound4Wins(R3T4);
  R4T2.innerHTML = R3T3.innerHTML; document.getElementById("series14").value = R3T3.innerHTML;});
R3T4.addEventListener("click", function G14T2() {
  Winner(R3T4); Loser(R3T3); ClearRound4Wins(R3T3);
  R4T2.innerHTML = R3T4.innerHTML; document.getElementById("series14").value = R3T4.innerHTML;});

// -- End Round 3 --


// series 15
R4T1.addEventListener("click", function G15T1() {
  Winner(R4T1); Loser(R4T2); document.getElementById("series15").value = R4T1.innerHTML;});

R4T2.addEventListener("click", function G15T1() {
  Winner(R4T2); Loser(R4T1); document.getElementById("series15").value = R4T2.innerHTML;});

// -- End Playoffs --

// -- Standings Tables --
function SortIt(id) {
  var ColNames = ["Name", "Points", "TPP"]
  for (let i=0; i<3; i++) {
      document.getElementById(i+"Col").style.display = "none";
      document.getElementById(i).style.display = "none";
    }
  document.getElementById(id+"Col").style.display = "inline-block";
  document.getElementById(id).style.display = "table-row-group";
}

function ShowBracket(img_name) {
  document.getElementById("personal-bracket").src = "bracket/static/images/Brackets/"+img_name+".png";
}
