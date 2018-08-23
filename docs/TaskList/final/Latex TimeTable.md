### Latex TimeTable

```latex
/documentclass{article}

/usepackage[landscape,a4paper]{geometry}
/usepackage{microtype}
/usepackage[default,semibold,light]{sourcesanspro}
/usepackage{realscripts}
/usepackage{parskip}
/pagestyle{empty}

/newcommand*{/roomone}{Adare Uniting Church Auditorium}
/newcommand*{/roomtwo}{Adare Uniting Church Hall}
/newcommand*{/roomfour}{Adare Uniting Church Foyer}
/newcommand*{/roomsix}{Adare Dining Room}
/newcommand*{/roomtwelve}{Bethany Hall}
/newcommand*{/roomfood}{/roomsix/slash/roomtwelve}
/newcommand*{/roommdgs}{Room listed on booklet cover}
/newcommand*{/roomseminars}{Rooms listed on p.~/pageref{seminars}}
/newcommand*{/roomworkshops}{Rooms listed on p.~/pageref{workshops}}

/newcommand*{/firstspeaker}{Gary Millar}
/newcommand*{/secondspeaker}{Reuben Salagaras}

/newcommand*{/timetablefont}{/scriptsize}

/newcommand*{/yscale}{0.862}

/newlength{/timewidth}
/settowidth{/timewidth}{/timetablefont/bfseries
  /addfontfeature{RawFeature=-pnum}00:00}
/addtolength{/timewidth}{4pt}

/newlength{/activitywidth}
/setlength{/activitywidth}{/textwidth}
/addtolength{/activitywidth}{-4/timewidth}
/addtolength{/activitywidth}{-14pt}
/setlength{/activitywidth}{0.25/activitywidth}

/usepackage[cmyk]{xcolor}
/definecolor{mdg}{cmyk}{0,0.3,0.24,0.03}
/definecolor{talk}{cmyk}{0.13,0,0,0}
/definecolor{coach}{cmyk}{0,0.02,0.22,0}
/definecolor{food}{cmyk}{0,0.2,0.41,0.06}
/definecolor{seminar}{cmyk}{0.08,0,0.11,0.04}
/definecolor{workshop}{cmyk}{0,0,0,0.11}

/usepackage{tikz}
/usetikzlibrary{positioning,chains}

/begin{document}

/begin{tikzpicture}[
    remember picture,
    overlay,
    node distance=0 cm,
    chain default direction=going below,
    inner sep=0pt,
    outer sep=1pt,
    font=/timetablefont,
    time/.style args={#1,#2}{
      anchor=north west,
      minimum width=/timewidth,
      minimum height=/yscale*#1cm-2pt,
      node contents={},
      append after command={
        node[anchor=north east, inner sep=0pt, outer sep=3pt,
        font=/timetablefont/bfseries/addfontfeature{RawFeature=-pnum}]
        at (/tikzlastnode.north east) {#2}
      },
      on chain
    },
    activity/.style args={#1,#2,#3}{
      anchor=north west,
      minimum width=/activitywidth,
      minimum height=/yscale*#1cm-2pt,
      node contents={},
      append after command={
        node[anchor=north west, inner sep=0pt, outer sep=3pt,
        text width=/activitywidth-6pt]
        at (/tikzlastnode.north west) {/textbf{#2}//#3}
      },
      on chain
    }
  ]
  /begin{scope}[start chain]
    /node (fri-time) [time={1,}];
    /node[time={10,}];
    /node[time={2,18:00}];
    /node[time={1.5,20:00}];
    /node[time={1,21:30}];
  /end{scope}
  /begin{scope}[start chain]
    /node (fri) [right=of fri-time.north east, activity={1,/Large/hfill
    Friday/hfill/strut,}];
    /node[activity={10,,}];
    /node[activity={2,Registration,/roomfour}];
    /node[activity={1.5,Talk 1: /firstspeaker,/roomone},fill=talk];
    /node[activity={1,Supper,/roomtwo}];
  /end{scope}
  /begin{scope}[start chain]
    /node (sat-time) [right=of fri.north east, time={1,}];
    /node[time={1,8:00}];
    /node[time={1.5,9:00}];
    /node[time={0.75,10:30}];
    /node[time={1.25,11:15}];
    /node[time={0.5,12:45}];
    /node[time={1.5,13:00}];
    /node[time={1.5,14:30}];
    /node[time={0.5,16:00}];
    /node[time={1.5,16:30}];
    /node[time={1.5,18:00}];
    /node[time={1.5,19:30}];
    /node[time={1.5,21:00}];
  /end{scope}
  /begin{scope}[start chain]
    /node (sat) [right=of sat-time.north east, activity={1,/Large/hfill
    Saturday/hfill/strut,}];
    /node[activity={1,Breakfast,/roomfood}, fill=food];
    /node[activity={1.5,Talk 2: /secondspeaker,/roomone}, fill=talk];
    /node[activity={0.75,Morning tea,}];
    /node[activity={1.25,Ministry Discussion Group 1,Room listed on booklet
    cover}, fill=mdg];
    /node[activity={0.5,Coach's briefing,}];
    /node[activity={1.5,Lunch,/roomfood}, fill=food];
    /node[activity={1.5,Free time/slash Coaching slot 1,}, fill=coach];
    /node[activity={0.5,Afternoon tea,}];
    /node[activity={1.5,Free time/slash Coaching slot 2,}, fill=coach];
    /node[activity={1.5,Dinner,/roomfood}, fill=food];
    /node[activity={1.5,Talk 3: /firstspeaker,/roomone}, fill=talk];
    /node[activity={1.5,Supper,/roomtwo}];
  /end{scope}
  /begin{scope}[start chain]
    /node (sun-time) [right=of sat.north east, time={1,}];
    /node[time={0.5,}];
    /node[time={1,8:30}];
    /node[time={1.25,9:30}];
    /node[time={0.5,10:45}];
    /node[time={1.25,11:15}];
    /node[time={1,12:30}];
    /node[time={1,13:30}];
    /node[time={1.5,14:30}];
    /node[time={0.5,16:00}];
    /node[time={1.5,16:30}];
    /node[time={1.5,18:00}];
    /node[time={2,19:30}];
    /node[time={1,21:30}];
  /end{scope}
  /begin{scope}[start chain]
    /node (sun) [right=of sun-time.north east, activity={1,/Large/hfill
    Sunday/hfill/strut,}];
    /node[activity={0.5,,}];
    /node[activity={1,Breakfast,/roomfood}, fill=food];
    /node[activity={1.25,Seminars,/roomseminars}, fill=seminar];
    /node[activity={0.5,Morning tea,}];
    /node[activity={1.25,Workshops,/roomworkshops}, fill=workshop];
    /node[activity={1,Lunch,/roomfood}, fill=food];
    /node[activity={1,Ministry Discussion Group 2,/roommdgs}, fill=mdg];
    /node[activity={1.5,Free time/slash Coaching slot 3,}, fill=coach];
    /node[activity={0.5,Afternoon tea,}];
    /node[activity={1.5,Free time/slash Coaching slot 4,}, fill=coach];
    /node[activity={1.5,Dinner,/roomfood}, fill=food];
    /node[activity={2,Talk 4: /secondspeaker,/roomone}, fill=talk];
    /node[activity={1,Supper,/roomtwo}];
  /end{scope}
  /begin{scope}[start chain]
    /node (mon-time) [right=of sun.north east, time={1,}];
    /node[time={0.5,}];
    /node[time={0.5,8:30}];
    /node[time={1,9:00}];
    /node[time={0.5,10:00}];
    /node[time={1,10:30}];
    /node[time={1.5,11:30}];
    /node[time={1,13:00}];
  /end{scope}
  /begin{scope}[start chain]
    /node[right=of mon-time.north east, activity={1,/Large/hfill
    Monday/hfill/strut,}];
    /node[activity={0.5,,}];
    /node[activity={0.5,Light breakfast,}];
    /node[activity={1,Ministry Discussion Group 3,/roommdgs}, fill=mdg];
    /node[activity={0.5,Personal reflection/slash prayer,}];
    /node[activity={1,Brunch,/roomtwo}, fill=food];
    /node[activity={1.5,Talk 5: /firstspeaker,/roomone}, fill=talk];
    /node[activity={1,Pack up and leave,}];
  /end{scope}
/end{tikzpicture}%

/end{document}
```
![vSLlc.png](https://i.stack.imgur.com/vSLlc.png)
