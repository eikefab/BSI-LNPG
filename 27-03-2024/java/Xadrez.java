public class Xadrez {

    public class Peca {

        private final String id;
        private final String cor;

        public Peca(String id, String cor) {
            this.id = id;
            this.cor = cor;
        }

        public String getId() {
            return id;
        }

        public String getCor() {
            return cor;
        }

    }

    Peca[][] tabuleiro;

    public Xadrez(Peca[][] tabuleiro) {
        this.tabuleiro = tabuleiro;
    }

    public Xadrez() {
        this(new Peca[][] {});
    }

    public void moverPeca() {

    }

    public void capturarPeca(Peca inimigo, int linha, int coluna) {

    }

    public boolean podeMoverPara(Peca peca, int posicao) {
        return false;
    }

    public Peca getPeca(int linha, int coluna) {
        return null;
    }

}
