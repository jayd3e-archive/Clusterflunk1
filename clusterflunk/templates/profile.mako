<%inherit file="layouts/profile_base.mako"/>

<%def name="page()">
    <div class="profile_view">
        <div class="inner">
            <div class="main_info">
                <img src="/static/img/portrait.png" />
                <div class="account_info">
                    <h1>jayd3e</h1>
                    <div class="info_piece"><strong>E-mail:</strong> jd.dallago@gmail.com</div>
                    <div class="info_piece"><strong>Join Date:</strong> August 23, 2007</div>
                    <div class="info_piece"><strong>Networks:</strong>
                        <ul class="network_list">
                            <li>Universe</li>
                            <li>University of Iowa</li>
                        </ul>
                    </div>
                </div>
                <div class="clear"></div>
            </div>
        </div>
    </div>
    <div class="top_section">
        <div class="posts_section">
            <h1>Posts (20)</h1>
            <ul class="posted">
                % for i in range(10):
                    <li><a href="#">Post #${i}</a></li>
                % endfor
            </ul>
        </div>
        <div class="groups_section">
            <h1>Groups (12)</h1>
            <ul class="grouped">
                % for i in range(10):
                    <li><a href="#">Group #${i}</a></li>
                % endfor
            </ul>
        </div>
        <div class="clear"></div>
    </div>
    <div class="bottom_section">
        <div class="solutions_section">
            <h1>Solutions (35)</h1>
            <ul class="solutioned">
                % for i in range(10):
                    <li><a href="#">Solution #${i}</a></li>
                % endfor
            </ul>
        </div>
        <div class="comments_section">
            <h1>Comments (3)</h1>
            <ul class="commented">
                % for i in range(10):
                    <li><a href="#">Comment #${i}</a></li>
                % endfor
            </ul>
        </div>
        <div class="clear"></div>
    </div>
</%def>