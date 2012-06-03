<%inherit file="../layouts/base.mako"/>
<%namespace name="util_side" file="../utilities/side.mako"/>

<%def name="page()">
    <div id="group_view">
        <h1>${group.name}</h1>
        <ul id="page_actions">
            <li>
                <a class="primary" href="/posts/create">Create Post</a>
            </li>
        </ul>
        <p>${group.description}</p>
    </div>
</%def>

<%def name="aside()">
    ${util_side.due()}
</%def>