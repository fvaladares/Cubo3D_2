import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import sys

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

colors = (
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
    (0, 1, 0),
    (1, 1, 1),
    (0, 1, 1),
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
    (1, 0, 0),
    (1, 1, 1),
    (0, 1, 1),
)

surfaces = (
    (0, 1, 2, 3),
    (3, 2, 7, 6),
    (6, 7, 5, 4),
    (4, 5, 1, 0),
    (1, 5, 7, 2),
    (4, 0, 3, 6)
)


# --- Função de Desenho ---

def Cube():
    # Desenha as arestas do cubo
    glBegin(GL_QUADS)

    for surface in surfaces:
        x = 0
        for vertex in surface:
            x += 1
            glColor3fv(colors[x])
            glVertex3fv(verticies[vertex])
    glEnd()


# Remova estes comentários para inserir as bordas no cubo.
#     glBegin(GL_LINES)
#     for edge in edges:
#         for vertex in edge:
#             glVertex3fv(verticies[vertex])
#     glEnd()


# --- Função Principal ---

def main():
    # 1. Inicializa o GLFW
    if not glfw.init():
        sys.exit()

    WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
    # Cria uma janela e seu contexto OpenGL
    window = glfw.create_window(WINDOW_WIDTH,
                                WINDOW_HEIGHT,
                                "GLFW OpenGL Cube",
                                None,
                                None)

    if not window:
        glfw.terminate()
        sys.exit()

    # Define o contexto da janela como o contexto de desenho atual
    glfw.make_context_current(window)

    # Este comando permite alterar a cor de fundo da tela.
    # glClearColor(1.0,
    #              1.0,
    #              1.0,
    #              1.0)

    # Ativa o teste de profundidade...
    glEnable(GL_DEPTH_TEST)

    # Configura a viewport
    glViewport(100,
               50,
               WINDOW_WIDTH,
               WINDOW_HEIGHT)

    # Configuração da projeção (igual ao gluPerspective do Pygame)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45,
                   (WINDOW_WIDTH / WINDOW_HEIGHT),
                   0.1,
                   50.0)
    glMatrixMode(GL_MODELVIEW)

    glLoadIdentity()

    # Move a câmera para trás
    glTranslatef(0.0,
                 0.0,
                 -5)

    while not glfw.window_should_close(window):
        # --- Processamento de Eventos (Entrada) ---
        # Sondar (poll) eventos de entrada (teclado, mouse, etc.)
        glfw.poll_events()

        # Adicionar verificação de entrada: Pressione ESC para fechar
        if glfw.get_key(window, glfw.KEY_ESCAPE) == glfw.PRESS:
            glfw.set_window_should_close(window, True)

        # --- Lógica de Renderização/Atualização ---

        # Rotação
        glRotatef(1,
                  5,
                  1,
                  1)

        # Limpa o buffer de cor e profundidade
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Desenha o cubo
        Cube()

        # --- Swap Buffers (Troca o buffer de exibição) ---
        # Equivalente ao pygame.display.flip()
        glfw.swap_buffers(window)

        # Nota sobre a espera: O GLFW geralmente não requer uma
        # pausa explícita como o pygame.time.wait(10)
        # a menos que você queira limitar o FPS de forma específica.

    # 6. Encerramento
    glfw.terminate()

# TODO(modifique o exemplo para capturar o envento do teclado (setas direcionais)
#  e altere o sentido de rotação do cubo, ou faça com que ele se movimente de acordo
# com a tecla pressionada.
if __name__ == "__main__":
    main()
