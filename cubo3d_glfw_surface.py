import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import sys

# --- Dados do Cubo (Não Mudam) ---

verticies = np.array([
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
], dtype=np.float32)

edges = (
    (0, 1), (0, 3), (0, 4),
    (2, 1), (2, 3), (2, 7),
    (6, 3), (6, 4), (6, 7),
    (5, 1), (5, 4), (5, 7)
)


def Cube():
    glBegin(GL_LINES)
    # glColor3f(0,0,1) # Removido para usar a cor definida no loop principal
    for edge in edges:
        for vertex_index in edge:
            glVertex3fv(verticies[vertex_index])
    glEnd()


# --- Função Principal ---

def main():
    if not glfw.init():
        sys.exit()

    WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
    window = glfw.create_window(WINDOW_WIDTH, WINDOW_HEIGHT, "GLFW Fixed Function Cube", None, None)

    if not window:
        glfw.terminate()
        sys.exit()

    glfw.make_context_current(window)

    # --- Configuração de Projeção Única ---
    # Define o modo de projeção
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    # Define a perspectiva (só precisa ser feito uma vez, a menos que a janela mude de tamanho)
    gluPerspective(45, (WINDOW_WIDTH / WINDOW_HEIGHT), 0.1, 50.0)

    # Retorna ao modo ModelView para trabalhar as transformações de modelo e câmera
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    # Habilita o teste de profundidade (bom para 3D)
    glEnable(GL_DEPTH_TEST)

    while not glfw.window_should_close(window):
        glfw.poll_events()
        if glfw.get_key(window, glfw.KEY_ESCAPE) == glfw.PRESS:
            glfw.set_window_should_close(window, True)

        # 1. Limpa a tela
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # 2. Inicializa a Matriz ModelView para este frame
        glLoadIdentity()

        # 3. Translação da Câmera (View Transformation)
        # Move o "mundo" 10 unidades para trás para que o cubo fique visível
        glTranslatef(0.0, 0.0, -10.0)

        # 4. Transformação do Modelo (Model Transformation)
        # Aplica a rotação contínua ao cubo
        glRotatef(1, 3, 1, 1)

        # 5. Define a cor do cubo
        glColor3f(0, 0.7, 0)  # Verde

        # 6. Desenha o cubo (que agora está rotacionado e centralizado)
        Cube()

        # 7. Troca de Buffer
        glfw.swap_buffers(window)
        # glfw.time.wait(10) não é necessário com GLFW

    glfw.terminate()


if __name__ == "__main__":
    main()