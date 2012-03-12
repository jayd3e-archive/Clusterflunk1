"""Added the Vote model.  Added 'score' to the Post model.

Revision ID: 1430624b38d3
Revises: 5a9e360f7378
Create Date: 2012-03-11 17:30:30.475962

"""

# downgrade revision identifier, used by Alembic.
down_revision = '5a9e360f7378'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('votes',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=True),
        sa.Column('post_id', sa.Integer(), nullable=True),
        sa.Column('vote', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.add_column(u'posts', sa.Column('score', sa.Integer(), nullable=True))
    ### end Alembic commands ###

def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('votes')
    op.drop_column(u'posts', 'score')
    ### end Alembic commands ###
