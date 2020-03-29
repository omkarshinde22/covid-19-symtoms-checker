## story_goodbye
* goodbye
    - utter_goodbye

## story_thankyou
* thankyou
    - utter_noworries



## happy_path
* greet
    - ask_corona
* inform{"corona": "sure"}    
    - enquiry
* inform{"enquiry":"for yourself"}
    - counter
    - enquiry

* inform{"enquiry":"male"}
    - counter
    - enquiry

* inform{"enquiry":"19 - 50"}
    - counter
    - enquiry



## Generated Story 503526406485602935
* greet
    - ask_corona
* inform{"corona": "sure"}
    - slot{"corona": "sure"}
    - enquiry
* enquiry{"enquiry": "for yourself"}
    - slot{"enquiry": "for yourself"}
    - counter
    - enquiry
* enquiry{"enquiry": "male"}
    - slot{"enquiry": "male"}
    - counter
    - enquiry
* enquiry{"enquiry": "19 - 50"}
    - slot{"enquiry": "19 - 50"}
    - counter
    - enquiry
* enquiry{"enquiry": "none of the above"}
    - slot{"enquiry": "none of the above"}
    - counter
    - enquiry
* enquiry{"enquiry": "none of the above"}
    - slot{"enquiry": "none of the above"}
    - counter
    - enquiry
* inform{"enquiry": "no"}
    - slot{"enquiry": "no"}
    - counter
    - enquiry
* inform{"enquiry": "no"}
    - slot{"enquiry": "no"}
    - counter
    - enquiry   
* inform{"enquiry": "no"}
    - slot{"enquiry": "no"}
    - counter
    - enquiry
* inform{"enquiry": "no"}
    - slot{"enquiry": "no"}
    - counter
    - enquiry
* inform{"enquiry": "no"}
    - slot{"enquiry": "no"}
    - counter
    - enquiry
* inform{"enquiry": "no"}
    - slot{"enquiry": "no"}
    - counter
    - enquiry
* inform{"enquiry": "no"}
    - slot{"enquiry": "no"}
    - counter
    - enquiry
* affirm{"affirm": "yes"}
    - ask_corona



## Generated Story -6176220288126818410
* greet
    - ask_corona
* inform{"corona": "sure"}
    - slot{"corona": "sure"}
    - enquiry
* enquiry{"enquiry": "for yourself"}
    - slot{"enquiry": "for yourself"}
    - counter
    - enquiry
* enquiry{"enquiry": "male"}
    - slot{"enquiry": "male"}
    - counter
    - enquiry
* enquiry{"enquiry": "19 - 50"}
    - slot{"enquiry": "19 - 50"}
    - counter
    - enquiry
* enquiry{"enquiry": "none of the above"}
    - slot{"enquiry": "none of the above"}
    - counter
    - enquiry
* enquiry{"enquiry": "none of the above"}
    - slot{"enquiry": "none of the above"}
    - counter
    - enquiry
* deny{"enquiry": "no"}
    - slot{"enquiry": "no"}
    - counter
    - enquiry
* affirm{"enquiry": "yes"}
    - slot{"enquiry": "yes"}
    - counter
    - enquiry
* affirm{"enquiry": "yes"}
    - slot{"enquiry": "yes"}
    - counter
    - enquiry
* deny{"enquiry": "no"}
    - slot{"enquiry": "no"}
    - counter
    - enquiry
* deny{"enquiry": "no"}
    - slot{"enquiry": "no"}
    - counter
    - enquiry
* deny{"enquiry": "no"}
    - slot{"enquiry": "no"}
    - counter
    - enquiry
* deny{"enquiry": "no"}
    - slot{"enquiry": "no"}
    - counter
    - enquiry
* affirm{"enquiry": "yes"}
    - slot{"enquiry": "yes"}
    - counter
    - utter_continue
* affirm{"affirm": "yes"}
    - ask_corona

