"""Added a 'created' column to the Article model.

Revision ID: 318fec9713f7
Revises: 44356600fc43
Create Date: 2012-03-13 13:03:39.939368

"""

# downgrade revision identifier, used by Alembic.
down_revision = '44356600fc43'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('articles', sa.Column('created', sa.DateTime(), nullable=True))
    ### end Alembic commands ###

def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('articles', 'created')
    ### end Alembic commands ###