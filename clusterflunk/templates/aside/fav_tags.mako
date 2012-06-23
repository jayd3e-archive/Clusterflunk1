<%def name="fav_tags()">
    <div class="fav_tags">
        <h6>Favorite Tags</h6>
        <ul class="tags">
            % for i in range(20):
            <li>
                tag_${i}
            </li>
            % endfor
        </ul>
    </div>
</%def>