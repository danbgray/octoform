<%inherit file="question.mako"/>
<%! from templates.html.encoding import markup %>

IF YOU ARE SEEING THIS IN A DOCUMENT, IT IS AN ERROR.

<%def name="header(q, state)"> 
${q.label|markup}
</%def>


<%def name="footer(q, state)"> 
${q}
% if state["form_has_errors"]:
% if field.errors:
    <DIV class="errors"> ${field.errors[0]} </DIV>
% endif
% endif

</%def>


<%def name="iter(q, state)"> 
</%def>
