FROM pyiron/base:2020-10-30

RUN rm ${HOME}/*
COPY . ${HOME}/

RUN conda env update -n base -f ${HOME}/environment.yml --prune && \
   conda clean --all -f -y && \
   npm cache clean --force


USER root
RUN apt-get update && \
    apt-get install build-essential && \
    apt-get clean
RUN fix-permissions /home/$DOCKER_USER &&\
    fix-permissions $CONDA_DIR
RUN rm -r LAMMPS-DAMASK-workflow Dockerfile environment.yml README.md
RUN fix-permissions /home/$DOCKER_USER
# Switch back to pyiron to avoid accidental container runs as root
USER $DOCKER_UID

WORKDIR $HOME
