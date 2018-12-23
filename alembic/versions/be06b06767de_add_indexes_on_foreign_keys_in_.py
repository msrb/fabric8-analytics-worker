"""Add indexes on foreign keys in WorkerResult and Analysis.

Revision ID: be06b06767de
Revises: a60f15a395e2
Create Date: 2017-05-26 06:06:23.030083

"""

# revision identifiers, used by Alembic.
revision = 'be06b06767de'
down_revision = 'a60f15a395e2'
branch_labels = None
depends_on = None

from alembic import op


def upgrade():
    """Upgrade the database to a newer revision."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_analyses_version_id'), 'analyses', ['version_id'], unique=False)
    op.create_index(op.f('ix_worker_results_analysis_id'), 'worker_results', ['analysis_id'],
                    unique=False)
    # ### end Alembic commands ###


def downgrade():
    """Downgrade the database to an older revision."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_worker_results_analysis_id'), table_name='worker_results')
    op.drop_index(op.f('ix_analyses_version_id'), table_name='analyses')
    # ### end Alembic commands ###
