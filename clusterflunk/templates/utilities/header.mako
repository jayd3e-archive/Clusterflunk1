<%!
    from clusterflunk.models.notifications import GroupInviteNotification
%>

<%def name="print_notification(notification)">
    <div class="notification">
        % if isinstance(notification, GroupInviteNotification):
            <div class="group_invite">
                <a class="dark" href="/profile/${notification.inviter.username}">
                    ${notification.inviter.username}
                </a>
                invited you to 
                <a class="dark" href="/groups/${notification.study_group.id}">
                    ${notification.study_group.name}
                </a>
            </div>
        % endif
    </div>
</%def>