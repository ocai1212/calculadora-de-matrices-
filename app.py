import numpy as np 
import streamlit as st 

st.set_page_config(page_title="resolutor de sistemas lineales", layout= "centered")
st.subheader("metodo de matriz inversa por adjunta (cofactores transpuesta)")

#seleccion del tamaño del sistema 
n = st.number_input(
    "selecciona el numero de varibles (N x N):",
    min_value = 2,
    max_value = 5,
    value=3,
    step=1,
)

#funciones para el calculo manual paso a paso 
def obtener_submatriz(matrix, i, j):
    """devuelve la submatriz eliminando la fila i y la columna j."""
    return np.delete(np.delete(matrix, i, axis=0), j, axis=1)

def matriz_cofactores(matrix):
    """calcula la matriz de cofactores C."""
    n_dim = matrix. shape[0]
    C = np.zeros((n_dim, n_dim))
    for i in range(n_dim):
        for j in range(n_dim):
            submat = obtener_submatriz(matrix, i, j)
            det_sub = np. linalg.det(submat)
            C[i, j] = ((-1)) ** ((i + j)) * det_sub

    return C
st.markdown("### 1. ingresa los coeficientes de la matriz A y el vector B")
col1, col2= st. columns ([3, 1])

with col1:
    st.write("**matriz de coeficientes (A)**")
    A = np.zeros((n, n))
    cols = st.columns(n)
    for i in range(n):
        for j in range(n):
            A[i, j] = cols[j].number_input(
                f"A[{i+1},{j+1}]", value=float(i+ j + 1), key=f"A_{i}_{j}"
            )
with col2:
    st.write("**vector (B)**")
    B = np.zeros((n, 1 ))
    for i in range (n):
        B[i, 0]= st.number_input(f"B[{i+1}]", value=1.0, key=f"B_{i}")
if st.button("Resolver sistemas", type ="primary"):
    det_A = np.linalg.det(A)

    st.markdown("---")
    st.markdown("###2. paso a paso del calculo")


    st.write(f"**paso 1: Determinante de A **")
    st.write(f"\det(A) = {det_A:.4f}")

    if np.isclose(det_A, 0): 
        st. error(
            "El determinante es cero (\det(A) =0). La matriz no es invertible y el sistema no tiene solucion unica."
        )

    else:
        # Paso 2: matriz de cofactores 
        C= matriz_cofactores(A)
        st.write("**Paso 2: matriz de cofactores (C)**")
        st.write(C)

        #Paso 3: matriz adjunta (transpuesta de la matriz de cofactores)
        Adj = C.T 
        st.write("**Paso 3: matriz adjunta C^T**")
        st.write(Adj)

        #paso 4: matriz inversa 
        A_inv= Adj / det_A
        st.write(
            "**Paso 4: matriz inversa **"
        )        
        st.write(A_inv)

        #Paso 5: solucion X = A^-1 * B 
        X = np.dot(A_inv, B)

        st.markdown("---")
        st.markdown("### 3. solucion final ")
        for i in range(n):
            st.success(f"**x_{i+1}** = {X[i, 0]:.4f}")


 
    
