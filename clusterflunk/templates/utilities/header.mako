<%!
    from clusterflunk.models.notifications import (
        GroupInviteNotification,
        StatusCommentNotification
    )
%>

<%def name="print_notification(notification)">
    <div class="notification">
        % if isinstance(notification, GroupInviteNotification):
            <div class="group_invite_notification">
                <a href="/profile/${notification.inviter.username}">
                    ${notification.inviter.username}
                </a>
                invited you to
                <a href="/groups/${notification.study_group.id}">
                    ${notification.study_group.name}
                </a>
            </div>
        % elif isinstance(notification, StatusCommentNotification):
            <div class="status_comment_notification">
                <a href="/profile/${notification.commenter.username}">
                    ${notification.commenter.username}
                </a>
                commented on a
                <a href="/statuses/${notification.status.id}">
                    status
                </a>
                you interacted with.
            </div>
        % endif
    </div>
</%def>