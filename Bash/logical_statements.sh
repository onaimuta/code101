#!/bin/bash
<<COMMENTS

Conditionals have many forms. The most basic form is: if expression then statement where 'statement' is only
executed if 'expression' evaluates to true. '2<1' is an expresion that evaluates to false, while '2>1' evaluates to
true.xs

Conditionals have other forms such as: if expression then statement1 else statement2. Here 'statement1' is
executed if 'expression' is true,otherwise 'statement2' is executed.

if expression1 then statement1 else
if expression2 then statement2 else statement3. In this form there's added only the "ELSE IF 'expression2'
THEN 'statement2'" which makes statement2 being executed if expression2 evaluates to true. The rest is as
you may imagine (see previous forms).

if [expression];
then
code if 'expression' is true.
fi

COMMENTS

read country

if ["country"="zimbabwe"]; then
    echo zimbo
    exit
elif ["country"="uganda"]
    echo ug
else

fi
exit
