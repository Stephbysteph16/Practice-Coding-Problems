// Found this solution online, I did not know about trie trees
// This problem only solvable with trie trees.

class TrieNode {
    char c;
    TrieNode left;
    TrieNode right;

    public TrieNode(char c) {
        this.c = c;
    }

    public void set(TrieNode node) {
        if (node.c == '0') {
            this.left = node;
        } else if (node.c == '1') {
            this.right = node;
        }
    }

    public TrieNode getChild(char c) {
        if (c == '0')
            return this.left;
        if (c == '1')
            return this.right;
        return null;
    }
}

class TrieTree {
    private TrieNode root;
    private int maxDepth = 0;

    public TrieTree(List<String> binaries) {
        root = new TrieNode('\0');
        for (String binary : binaries) {
            TrieNode cur = root;
            for (char c : binary.toCharArray()) {
                TrieNode node = cur.getChild(c);
                if (node == null) {
                    node = new TrieNode(c);
                    cur.set(node);
                }
                cur = node;
            }
        }
    }

    public int maxDepth() {
        maxDepth(root);
        return this.maxDepth;
    }

    private int maxDepth(TrieNode node) {
        if (node == null)
            return 0;
        int left = maxDepth(node.left);
        int right = maxDepth(node.right);
        if (left > 0 && right > 0) {
            this.maxDepth = Math.max(this.maxDepth, left + right);
        }

        return 1 + Math.max(left, right);
    }
}

public class MaxDifference {
    public static void main(String[] args) {
        String[] binaries = { "1011100", "1011011", "1001111", "0111111" };
        TrieTree t = new TrieTree(Arrays.asList(binaries));
        System.out.println(t.maxDepth());

    }

}