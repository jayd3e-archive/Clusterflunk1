<%def name="error(form, field)">
    % if field in form.errors:
        % for error in form.errors[field]:
            <div class="error">${error}</div>
        % endfor
    % endif
</%def>