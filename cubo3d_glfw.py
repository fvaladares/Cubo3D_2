import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import sys  # Para usar sys.exit() ao fechar a aplicação

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


# --- Função de Desenho ---

def Cube():
    # Desenha as arestas do cubo
    glBegin(GL_LINES)
    # A cor de 0,0,1 (azul) é definida na linha anterior no código original,
    # mas o PyOpenGL tende a reter o último glColor3f.
    # É melhor definir a cor aqui ou mantê-la fora para ser alterada no loop principal.
    # Se você quiser que o cubo seja azul (como no seu código):
    # glColor3f(0, 0, 1)

    for edge in edges:
        for vertex_index in edge:
            glVertex3fv(verticies[vertex_index])
    glEnd()


# --- Função Principal ---

def main():
    # 1. Inicializa o GLFW
    if not glfw.init():
        sys.exit()

    WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
    # Cria uma janela e seu contexto OpenGL
    window = glfw.create_window(WINDOW_WIDTH, WINDOW_HEIGHT, "GLFW OpenGL Cube", None, None)

    if not window:
        glfw.terminate()
        sys.exit()

    # Define o contexto da janela como o contexto de desenho atual
    glfw.make_context_current(window)

    # Configura a viewport
    glViewport(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)

    # Configuração da projeção (igual ao gluPerspective do Pygame)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, (WINDOW_WIDTH / WINDOW_HEIGHT), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)
    # Move a câmera para trás (igual ao glTranslatef no seu código)
    # glTranslatef(0.0, 0.0, -10)
    glLoadIdentity()

    # Move a câmera para trás (igual ao glTranslatef no seu código)
    glTranslatef(0.0, 0.0, -10)

    # 2. Loop Principal
    while not glfw.window_should_close(window):
        # --- 3. Processamento de Eventos (Entrada) ---
        # Sondar (poll) eventos de entrada (teclado, mouse, etc.)
        glfw.poll_events()

        # Adicionar verificação de entrada: Pressione ESC para fechar
        if glfw.get_key(window, glfw.KEY_ESCAPE) == glfw.PRESS:
            glfw.set_window_should_close(window, True)

        # --- 4. Lógica de Renderização/Atualização ---

        # Rotação (igual ao glRotatef no seu código)
        glRotatef(1, 3, 1, 1)

        # Limpa o buffer de cor e profundidade
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Define a cor para o cubo (o verde em (0, 0.7, 0))
        glColor3f(0, 0.7, 0)

        # Desenha o cubo
        Cube()

        # --- 5. Swap Buffers (Troca o buffer de exibição) ---
        # Equivalente ao pygame.display.flip()
        glfw.swap_buffers(window)

        # Nota sobre a espera: O GLFW geralmente não requer uma
        # pausa explícita como o pygame.time.wait(10)
        # a menos que você queira limitar o FPS de forma específica.

    # 6. Encerramento
    glfw.terminate()


if __name__ == "__main__":
    main()