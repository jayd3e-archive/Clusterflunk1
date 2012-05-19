"""Added a new notification class called StatusCommentNotification, which tracks when a user needs to be notififed about a status being commented on.

Revision ID: 174e9dced42
Revises: 1e508c63d41a
Create Date: 2012-04-27 20:45:17.563292

"""

# downgrade revision identifier, used by Alembic.
revision = '174e9dced42'
down_revision = '1e508c63d41a'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('status_comment_notifications',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('comment_id', sa.Integer(), nullable=True),
    sa.Column('status_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['comment_id'], ['comments.id'], ),
    sa.ForeignKeyConstraint(['id'], ['notification_items.id'], ),
    sa.ForeignKeyConstraint(['status_id'], ['statuses.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###

def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('status_comment_notifications')
    ### end Alembic commands ###