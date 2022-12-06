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

var R2HIClear = [HI1,HI2,HI3,HI4,HI5,HI6,HI7,HI8];
var R3HIClear = [HI9,HI10,HI11,HI12];
var R4HIClear = [HI13,HI14];

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

function Winner(id, value) {
  if (value != "") {
    id.classList.remove("loser");
    id.classList.add("winner");}
}

function Loser(id, value) {
  if (value != "") {
    id.classList.remove("winner");
    id.classList.add("loser");}
}

function ClearRound2Wins(clearteam) {
  for (let i=0; i<R2HIClear.length; i++) {
    if (R2HIClear[i].value == clearteam) {
      R2HIClear[i].value = "";
      Round2Teams[i].innerHTML = "";
      Round2Teams[i].classList.remove("loser","winner");}
  }
}

function ClearRound3Wins(clearteam) {
  for (let i=0; i<R3HIClear.length; i++) {
    if (R3HIClear[i].value == clearteam) {
      R3HIClear[i].value = "";
      Round3Teams[i].innerHTML = "";
      Round3Teams[i].classList.remove("loser","winner");}
  }
}

function ClearRound4Wins(clearteam) {
  for (let i=0; i<R4HIClear.length; i++) {
    if (R4HIClear[i].value == clearteam) {
      R4HIClear[i].value = "";
      Round4Teams[i].innerHTML = "";
      Round4Teams[i].classList.remove("loser","winner");}
  }
  if (HI15.value == clearteam){
    HI15.value = "";
  }
}

function ClearField(name) {
  if (name.value == "First and last name...") {
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
const R1T1Txt = document.getElementById("R1T1-team");
const R1T2Txt = document.getElementById("R1T2-team");

R1T1.addEventListener("click", function G1T1() {
  Winner(R1T1, 1); Loser(R1T2, 1); ClearRound2Wins(R1T2Txt.innerHTML); ClearRound3Wins(R1T2Txt.innerHTML); ClearRound4Wins(R1T2Txt.innerHTML);
  R2T1.innerHTML = R1T1.innerHTML; HI1.value = R1T1Txt.innerHTML;});
R1T2.addEventListener("click", function G1T2() {
  Winner(R1T2, 1); Loser(R1T1, 1); ClearRound2Wins(R1T1Txt.innerHTML); ClearRound3Wins(R1T1Txt.innerHTML); ClearRound4Wins(R1T1Txt.innerHTML);
  R2T1.innerHTML = R1T2.innerHTML; HI1.value = R1T2Txt.innerHTML;});

// series 2
const R1T3Txt = document.getElementById("R1T3-team");
const R1T4Txt = document.getElementById("R1T4-team");

R1T3.addEventListener("click", function G2T1() {
  Winner(R1T3, 1); Loser(R1T4, 1); ClearRound2Wins(R1T4Txt.innerHTML); ClearRound3Wins(R1T4Txt.innerHTML); ClearRound4Wins(R1T4Txt.innerHTML);
  R2T2.innerHTML = R1T3.innerHTML; HI2.value = R1T3Txt.innerHTML;});
R1T4.addEventListener("click", function G2T2() {
  Winner(R1T4, 1); Loser(R1T3, 1); ClearRound2Wins(R1T3Txt.innerHTML); ClearRound3Wins(R1T3Txt.innerHTML); ClearRound4Wins(R1T3Txt.innerHTML);
  R2T2.innerHTML = R1T4.innerHTML; HI2.value = R1T4Txt.innerHTML;});

// series 3
const R1T5Txt = document.getElementById("R1T5-team");
const R1T6Txt = document.getElementById("R1T6-team");

R1T5.addEventListener("click", function G3T1() {
  Winner(R1T5, 1); Loser(R1T6, 1); ClearRound2Wins(R1T6Txt.innerHTML); ClearRound3Wins(R1T6Txt.innerHTML); ClearRound4Wins(R1T6Txt.innerHTML);
  R2T3.innerHTML = R1T5.innerHTML; HI3.value = R1T5Txt.innerHTML;});
R1T6.addEventListener("click", function G3T2() {
  Winner(R1T6, 1); Loser(R1T5, 1); ClearRound2Wins(R1T5Txt.innerHTML); ClearRound3Wins(R1T5Txt.innerHTML); ClearRound4Wins(R1T5Txt.innerHTML);
  R2T3.innerHTML = R1T6.innerHTML; HI3.value = R1T6Txt.innerHTML;});

// series 4
const R1T7Txt = document.getElementById("R1T7-team");
const R1T8Txt = document.getElementById("R1T8-team");

R1T7.addEventListener("click", function G4T1() {
  Winner(R1T7, 1); Loser(R1T8, 1); ClearRound2Wins(R1T8Txt.innerHTML); ClearRound3Wins(R1T8Txt.innerHTML); ClearRound4Wins(R1T8Txt.innerHTML);
  R2T4.innerHTML = R1T7.innerHTML; HI4.value = R1T7Txt.innerHTML;});
R1T8.addEventListener("click", function G4T2() {
  Winner(R1T8, 1); Loser(R1T7, 1); ClearRound2Wins(R1T7Txt.innerHTML); ClearRound3Wins(R1T7Txt.innerHTML); ClearRound4Wins(R1T7Txt.innerHTML);
  R2T4.innerHTML = R1T8.innerHTML; HI4.value = R1T8Txt.innerHTML;});

// series 5
const R1T9Txt = document.getElementById("R1T9-team");
const R1T10Txt = document.getElementById("R1T10-team");

R1T9.addEventListener("click", function G5T1() {
  Winner(R1T9, 1); Loser(R1T10, 1); ClearRound2Wins(R1T10Txt.innerHTML); ClearRound3Wins(R1T10Txt.innerHTML); ClearRound4Wins(R1T10Txt.innerHTML);
  R2T5.innerHTML = R1T9.innerHTML; HI5.value = R1T9Txt.innerHTML;});
R1T10.addEventListener("click", function G5T2() {
  Winner(R1T10, 1); Loser(R1T9, 1); ClearRound2Wins(R1T9Txt.innerHTML); ClearRound3Wins(R1T9Txt.innerHTML); ClearRound4Wins(R1T9Txt.innerHTML);
  R2T5.innerHTML = R1T10.innerHTML; HI5.value = R1T10Txt.innerHTML;});

// series 6
const R1T11Txt = document.getElementById("R1T11-team");
const R1T12Txt = document.getElementById("R1T12-team");

R1T11.addEventListener("click", function G6T1() {
  Winner(R1T11, 1); Loser(R1T12, 1); ClearRound2Wins(R1T12Txt.innerHTML); ClearRound3Wins(R1T12Txt.innerHTML); ClearRound4Wins(R1T12Txt.innerHTML);
  R2T6.innerHTML = R1T11.innerHTML; HI6.value = R1T11Txt.innerHTML;});
R1T12.addEventListener("click", function G6T2() {
  Winner(R1T12, 1); Loser(R1T11, 1); ClearRound2Wins(R1T11Txt.innerHTML); ClearRound3Wins(R1T11Txt.innerHTML); ClearRound4Wins(R1T11Txt.innerHTML);
  R2T6.innerHTML = R1T12.innerHTML; HI6.value = R1T12Txt.innerHTML;});

// series 7
const R1T13Txt = document.getElementById("R1T13-team");
const R1T14Txt = document.getElementById("R1T14-team");

R1T13.addEventListener("click", function G7T1() {
  Winner(R1T13, 1); Loser(R1T14, 1); ClearRound2Wins(R1T14Txt.innerHTML); ClearRound3Wins(R1T14Txt.innerHTML); ClearRound4Wins(R1T14Txt.innerHTML);
  R2T7.innerHTML = R1T13.innerHTML; HI7.value = R1T13Txt.innerHTML;});
R1T14.addEventListener("click", function G7T2() {
  Winner(R1T14, 1); Loser(R1T13, 1); ClearRound2Wins(R1T13Txt.innerHTML); ClearRound3Wins(R1T13Txt.innerHTML); ClearRound4Wins(R1T13Txt.innerHTML);
  R2T7.innerHTML = R1T14.innerHTML; HI7.value = R1T14Txt.innerHTML;});

// series 8
const R1T15Txt = document.getElementById("R1T15-team");
const R1T16Txt = document.getElementById("R1T16-team");

R1T15.addEventListener("click", function G8T1() {
  Winner(R1T15, 1); Loser(R1T16, 1); ClearRound2Wins(R1T16Txt.innerHTML); ClearRound3Wins(R1T16Txt.innerHTML); ClearRound4Wins(R1T16Txt.innerHTML);
  R2T8.innerHTML = R1T15.innerHTML; HI8.value = R1T15Txt.innerHTML;});
R1T16.addEventListener("click", function G8T2() {
  Winner(R1T16, 1); Loser(R1T15, 1); ClearRound2Wins(R1T15Txt.innerHTML); ClearRound3Wins(R1T15Txt.innerHTML); ClearRound4Wins(R1T15Txt.innerHTML);
  R2T8.innerHTML = R1T16.innerHTML; HI8.value = R1T16Txt.innerHTML;});

// -- End Round 1 --


// series 9
R2T1.addEventListener("click", function G9T1() {
  Winner(R2T1, HI1.value); Loser(R2T2, HI2.value); ClearRound3Wins(HI2.value); ClearRound4Wins(HI2.value);
  R3T1.innerHTML = R2T1.innerHTML; HI9.value = HI1.value;});
R2T2.addEventListener("click", function G9T2() {
  Winner(R2T2, HI2.value); Loser(R2T1, HI1.value); ClearRound3Wins(HI1.value); ClearRound4Wins(HI1.value);
  R3T1.innerHTML = R2T2.innerHTML; HI9.value = HI2.value;});

// series 10
R2T3.addEventListener("click", function G10T1() {
  Winner(R2T3, HI3.value); Loser(R2T4, HI4.value); ClearRound3Wins(HI4.value); ClearRound4Wins(HI4.value);
  R3T2.innerHTML = R2T3.innerHTML; HI10.value = HI3.value;});
R2T4.addEventListener("click", function G10T2() {
  Winner(R2T4, HI4.value); Loser(R2T3, HI3.value); ClearRound3Wins(HI3.value); ClearRound4Wins(HI3.value);
  R3T2.innerHTML = R2T4.innerHTML; HI10.value = HI4.value;});

// series 11
R2T5.addEventListener("click", function G11T1() {
  Winner(R2T5, HI5.value); Loser(R2T6, HI6.value); ClearRound3Wins(HI6.value); ClearRound4Wins(HI6.value);
  R3T3.innerHTML = R2T5.innerHTML; HI11.value = HI5.value;});
R2T6.addEventListener("click", function G11T2() {
  Winner(R2T6, HI6.value); Loser(R2T5, HI5.value); ClearRound3Wins(HI5.value); ClearRound4Wins(HI5.value);
  R3T3.innerHTML = R2T6.innerHTML; HI11.value = HI6.value;});

// series 12
R2T7.addEventListener("click", function G12T1() {
  Winner(R2T7, HI7.value); Loser(R2T8, HI8.value); ClearRound3Wins(HI8.value); ClearRound4Wins(HI8.value);
  R3T4.innerHTML = R2T7.innerHTML; HI12.value = HI7.value;});
R2T8.addEventListener("click", function G12T2() {
  Winner(R2T8, HI8.value); Loser(R2T7, HI7.value); ClearRound3Wins(HI7.value); ClearRound4Wins(HI7.value);
  R3T4.innerHTML = R2T8.innerHTML; HI12.value = HI8.value;});

// -- End Round 2 --


// series 13
R3T1.addEventListener("click", function G13T1() {
  Winner(R3T1, HI9.value); Loser(R3T2, HI10.value); ClearRound4Wins(HI10.value);
  R4T1.innerHTML = R3T1.innerHTML; HI13.value = HI9.value;});
R3T2.addEventListener("click", function G13T2() {
  Winner(R3T2, HI10.value); Loser(R3T1, HI9.value); ClearRound4Wins(HI9.value);
  R4T1.innerHTML = R3T2.innerHTML; HI13.value = HI10.value;});

// series 14
R3T3.addEventListener("click", function G14T1() {
  Winner(R3T3, HI11.value); Loser(R3T4, HI12.value); ClearRound4Wins(HI12.value);
  R4T2.innerHTML = R3T3.innerHTML; HI14.value = HI11.value;});
R3T4.addEventListener("click", function G14T2() {
  Winner(R3T4, HI12.value); Loser(R3T3, HI11.value); ClearRound4Wins(HI11.value);
  R4T2.innerHTML = R3T4.innerHTML; HI14.value = HI12.value;});

// -- End Round 3 --


// series 15
R4T1.addEventListener("click", function G15T1() {
  Winner(R4T1, HI13.value); Loser(R4T2, HI14.value);
  HI15.value = HI13.value;});

R4T2.addEventListener("click", function G15T1() {
  Winner(R4T2, HI14.value); Loser(R4T1, HI13.value);
  HI15.value = HI14.value;});

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
};

function ShowBracket(img_name) {
  document.getElementById("personal-bracket").src = "bracket/static/images/Brackets/"+img_name+".png";
};

// -- Expanding Scores --

function Expand(id) {
  let prefix = id.id;

  if (id.innerText == ">>") {
    id.innerText = "<<";
    for (let i=0; i<7; i++) {
      document.getElementById(prefix+"Hd"+String(i+1)).style.display = "table-cell";
      document.getElementById(prefix+"T1C"+String(i+1)).style.display = "table-cell";
      document.getElementById(prefix+"T2C"+String(i+1)).style.display = "table-cell";
    }
  } else {
    id.innerText = ">>";
    for (let i=0; i<7; i++) {
      document.getElementById(prefix+"Hd"+String(i+1)).style.display = "none";
      document.getElementById(prefix+"T1C"+String(i+1)).style.display = "none";
      document.getElementById(prefix+"T2C"+String(i+1)).style.display = "none";
    }
  }
};
