# Git y control de versiones

Git es un sistema distribuido de control de versiones que permite registrar cambios y colaborar en proyectos de software. Un repositorio contiene el historial de versiones y el estado de los archivos.

El comando `git add` prepara cambios para el próximo commit. `git commit` registra una instantánea de los cambios preparados en el historial local del repositorio. `git push` envía commits locales a un repositorio remoto, por ejemplo GitHub. `git pull` obtiene cambios remotos e intenta integrarlos en la rama local. `git clone` crea una copia local de un repositorio remoto.

Una rama permite desarrollar cambios de forma aislada. Un merge integra historiales de ramas diferentes. Un conflicto aparece cuando Git no puede combinar automáticamente cambios incompatibles y requiere que una persona edite los archivos y marque la resolución. El archivo `.gitignore` indica qué archivos o carpetas no deberían incorporarse al seguimiento, como entornos virtuales y archivos `.env` con secretos.
